#!/usr/bin/env -S node --no-warnings --loader ts-node/esm
/**
 * Wechaty - Conversational RPA SDK for Chatbot Makers.
 *  - https://github.com/wechaty/wechaty
 */
// https://stackoverflow.com/a/42817956/1123955
// https://github.com/motdotla/dotenv/issues/89#issuecomment-587753552
import 'dotenv/config.js'
import {PythonShell} from 'python-shell';
var response;
import {
  Contact,
  Message,
  ScanStatus,
  WechatyBuilder,
  log,
}                  from 'wechaty'

import qrcodeTerminal from 'qrcode-terminal'

function delay(ms: number) {
    return new Promise( resolve => setTimeout(resolve, ms) );
}

function onScan (qrcode: string, status: ScanStatus) {
  if (status === ScanStatus.Waiting || status === ScanStatus.Timeout) {
    const qrcodeImageUrl = [
      'https://wechaty.js.org/qrcode/',
      encodeURIComponent(qrcode),
    ].join('')
    log.info('StarterBot', 'onScan: %s(%s) - %s', ScanStatus[status], status, qrcodeImageUrl)

    qrcodeTerminal.generate(qrcode, { small: true })  // show qrcode on console

  } else {
    log.info('StarterBot', 'onScan: %s(%s)', ScanStatus[status], status)
  }
}

function onLogin (user: Contact) {
  log.info('StarterBot', '%s login', user)
}

function onLogout (user: Contact) {
  log.info('StarterBot', '%s logout', user)
}


let text="";
let first = true;
let timer = 3;
let mode =3;
let preMode = mode;
let modeCGPT = false;
let instant = false;
let CGPTOnUse= false;
async function onMessage (msg: Message) {
  log.info('StarterBot', msg.toString())
  if (msg.self()==true) {return;}
  
  if(msg.text().includes("#mute")){
    if(mode == -2) {
    msg.say("Already muted")
    return
    }
    preMode = mode  
    mode=-2;
    msg.say("ok")  
    return;
  }
  
  if(msg.text().includes("#unmute")){
    if(mode!=-2) {
    msg.say("Already unmuted") 
    return
    }
    mode = preMode
    msg.say("I am baka!")  
    return;
  }
  
  if((msg.text().toLowerCase().includes("#mode"))||(msg.text().toLowerCase().includes("#help"))){
    msg.say("mode:" +mode+ " preMode:"+preMode + " CGPTOnUse:"+CGPTOnUse)
    msg.say("#mute=-2; #RAND=-1; #YUAN=0; #OPENAI=1; #BLOOM=3;")
    return;
  }  
  
  if((msg.text().toLowerCase().includes("#blm")||msg.text().toLowerCase().includes("#bloom"))){
    mode=3;
    msg.say("Model:BLOOM")  
    return;
  }
   
  if (msg.text().toLowerCase().includes("#open")){
    mode = 1;
    msg.say("Model:OPENAI")
    return;
  }
  
  if(msg.text().toLowerCase().includes("#yuan")){
    mode=0;
    msg.say("Model:YUAN")  
    return;
  }
  
  if(msg.text().toLowerCase().includes("#rand")){
    mode=0;
    msg.say("Model:random")  
    return;
  }
  
  if(msg.text().toLowerCase().includes("#reset"){
    resetAllVar()
  }
      
  if(msg.text().startsWith("#")) return;
    
  log.info("Msg type= "+msg.type());       
    
  if (msg.type() == "2"){
    text = "我发一段语音，[VOICET2]，听得到吗";
    sendMessage(msg);
    return;
  }
  
  if (msg.type() == "6"){
    text = "你的眼睛看不到[IMGT6]是图片";
    sendMessage(msg);
    return;
  }
  
  if (msg.type() !="7") return;
  
 
  if (first == true) {text = msg.text();}
  else {text = text + " " + msg.text();}
  log.info("Msg="+text);
     
  if (text.startsWith("::")||text.startsWith("：：")||modeCGPT==true){
    if (CGPTOnUse==true&&(text.startsWith("::")||text.startsWith("：："))) {
    msg.say("Wait, I am thinking about your last question.");
    return;
    }
    modeCGPT = true;
    log.info("CGPT mode");
    text = text.replace("::","");
    if (text.includes(",.")||text.includes("，。")) {
    instant = true;
    text = text.replace(",.","").replace("，。","");
    } else msg.say("Yes, I am listening");
    
    log.info("Collected text:"+text);
    if (first==true){
      timer = 15
      first = false;
      while (timer > 0){
        if (instant == false) await delay(3000);
        timer --;
        log.info("Less timer count:"+ timer);
    }
    msg.say("I see, let me ponder and I will answer.")
    sendMessageCGPT(msg);
    } else {
    if (timer>10) return;
    timer +=5 ;
    log.info("More timer count:"+ timer);    
    }
    return;
  } else {
    if(
    first==true
    &&(text.length > 10 || ['?', '？', '!', '！', '.', '。'].some(mark => msg.text().includes(mark)))
      ) instant = true;
 
    if (first==true){
      first = false;
      while (timer > 0){
        if (instant == false) await delay(3000);
        timer --;
        log.info("Less timer count:"+ timer);
      }
    sendMessage(msg);
    } else {
    if (timer>2) return;
    timer ++;
    log.info("More timer count:"+ timer);    
    }
  }
  
}

async function resetVar(){
  text="";
  first = true;
  instant = false;
  timer = 3;
}

async function resetCGPTVar(){
  modeCGPT = false;
  CGPTOnUse= false;
}


async function resetAllVar(){
  resetVar();
  resetCGPTVar();
}


async function sendMessage(msg){
  log.info("gotta run with " + text);
  var pyshell;
    if (mode==3) {pyshell = new PythonShell('blm.py'); log.info("BLOOM");}
    if (mode==1) {pyshell = new PythonShell('open.py'); log.info("OPEN");}
    if (mode==0) {pyshell = new PythonShell('yuan.py'); log.info("YUAN");}
    if (mode==-1) {
      if (Math.round(Math.random())==1) {pyshell = new PythonShell('yuan.py'); log.info("YUAN");}
      else {pyshell = new PythonShell('blm.py'); log.info("BLOOM");}
    }
    pyshell.send(text);
    resetVar();
    await pyshell.on('message', function (response) {
      if (response!=null){
        log.info("Response: "+response);
        if (response.includes("请重试")
          ||response.includes("模型返回为空")
          ||response.includes("[IMGT6]")
          ||response.includes("[VOICET2]")
          ) return;
      try {
        msg.say(response.replace(/\r?/g,'').replace(/[“”"。，？?！!]|您/g, '').replace(/[!！]/g, '啊').replace('A:','').replace('A：',''));
        return;
      }
      catch(err) {log.info(err);}
      return;
      }else return;
    });

}

async function sendMessageCGPT(msg){
  log.info("gotta run CGPT with " + text);
  CGPTOnUse=true;
  var pyshell;
  pyshell = new PythonShell('CGPT.py'); log.info("CGPT");
  pyshell.send(text);
  resetVar();
  modeCGPT==false;
    await pyshell.on('message', function (response) {
      CGPTOnUse=false;
      if (response!=null) log.info("Response: "+response);
      try {
      msg.say(response);
      return;
      } catch(err) {log.info(err);}
    });
}


const bot = WechatyBuilder.build({
  name: 'ding-dong-bot',
  puppet: 'wechaty-puppet-whatsapp'
})

bot.on('scan',    onScan)
bot.on('login',   onLogin)
bot.on('logout',  onLogout)
bot.on('message', onMessage)

bot.start()
  .then(() => log.info('StarterBot', 'Starter Bot Started.'))
  .catch(e => log.error('StarterBot', e))
