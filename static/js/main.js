var jbody=document.getElementById("divbody");
var jdivbut=document.getElementById("divbut");
var jbkimg=document.getElementById("bkimg");
var jtopbut1=document.getElementById("topbut1");
var jtopbut2=document.getElementById("topbut2");
var jtopbut3=document.getElementById("topbut3");
var jtopbut4=document.getElementById("topbut4");
var jside=document.getElementById("sidemenu");
var jsb=document.getElementById("sideback");
var jside1=document.getElementById("side1");
var jside2=document.getElementById("side2");
var jside3=document.getElementById("side3");
var jside4=document.getElementById("side4");
var jmain=document.getElementById("framesite");
var jmf=document.getElementById("mf");
var ontop = 1;
var temp1 = document.body.clientWidth;
var temp2 = window.screen.height ;
var temp3;

function framepo() {
  temp1 = document.body.clientWidth;
  temp2 = window.screen.height ;
  temp1 = Math.floor((temp1 - 1366) / 2 + 250);
  temp2 = Math.floor(temp2-200);
  temp3 = temp1 + 500;
  jmain.style.left = temp1 + "px";
  jmf.style.height = temp2 + "px";
}

function animatego(element,target){
  //清理定时器
  clearInterval(element.timeId);
  element.timeId = setInterval(function () {
    //获取元素的当前位置
    var current = element.offsetLeft;
    //移动的步数
    var step = 30;
    step = target > current ? step : -step;
    current += step;
    if (Math.abs(current - target) > Math.abs(step)) {
      element.style.left = current + "px";
    } else {
      clearInterval(element.timeId);
      element.style.left = target + "px";
    }
  }, 20);
}

function butout() {
  if (ontop === 1) {jbkimg.src="/static/img/layer0.png";}
}
function but1on(){
  if (ontop===1) {jbkimg.src="/static/img/layer1.png";}
}
function but2on(){
  if (ontop===1) {jbkimg.src="/static/img/layer2.png";}
}
function but3on(){
  if (ontop===1) {jbkimg.src="/static/img/layer3.png";}
}
function but4on(){
  if (ontop===1) {jbkimg.src="/static/img/layer4.png";}
}

function sideout() {
  jsb.src="/static/img/sideback.png";
  if (posi!==1){jside1.src="/static/img/side1.png";}
  if (posi!==2){jside2.src="/static/img/side2.png";}
  if (posi!==3){jside3.src="/static/img/side3.png";}
  if (posi!==4){jside4.src="/static/img/side4.png";}
}
function sb(){jsb.src="/static/img/sidebackon.png";}
function s1(){jside1.src="/static/img/side1on.png";}
function s2(){jside2.src="/static/img/side2on.png";}
function s3(){jside3.src="/static/img/side3on.png";}
function s4(){jside4.src="/static/img/side4on.png";}

function s1c(){posi=1;jmf.src="/static/pages/page1.html";}
function s2c(){posi=2;jmf.src="/static/pages/page2.html";}
function s3c(){posi=3;jmf.src="/static/pages/page3.html";}
function s4c(){posi=4;jmf.src="/static/pages/page4.html";}

function jbkt(){
  if (ontop===0){
    ontop=1;
    jdivbut.style.left="30px";
    jside.style.display="none";
    jmain.style.display="none";
    posi=1;jmf.src="/static/pages/page1.html";
  }
}

function but1click() {
  if(ontop===1) {
    jbkimg.src = "/static/img/layer0.png";
    ontop = 0;
    posi = 1;
    jside1.src = "/static/img/side1on.png";
    jmain.style.display = "block";
    jmf.src = "/static/pages/page1.html";
    jside.style.display = "block";
    framepo();jdivbut.style.left = temp3 + "px";
  }
}
function but2click() {
  if(ontop===1) {
    jbkimg.src = "/static/img/layer0.png";
    ontop = 0;
    posi = 2;
    jside2.src = "/static/img/side2on.png";
    jmain.style.display = "block";
    jmf.src = "/static/pages/page2.html";
    jside.style.display = "block";
    framepo();jdivbut.style.left = temp3 + "px";
  }
}
function but3click() {
  if(ontop===1) {
    jbkimg.src = "/static/img/layer0.png";
    ontop = 0;
    posi = 3;
    jside3.src = "/static/img/side3on.png";
    jmain.style.display = "block";
    jmf.src = "/static/pages/page3.html";
    jside.style.display = "block";
    framepo();jdivbut.style.left = temp3 + "px";
  }
}
function but4click() {
  if(ontop===1) {
    jbkimg.src = "/static/img/layer0.png";
    ontop = 0;
    posi = 4;
    jside4.src = "/static/img/side4on.png";
    jmain.style.display = "block";
    jmf.src = "/static/pages/page4.html";
    jside.style.display = "block";
    framepo();jdivbut.style.left = temp3 + "px";
  }
}
