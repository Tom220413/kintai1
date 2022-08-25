document.getElementById("nowtime").innerHTML = showTime();
setInterval('showTime()',1000);
function showTime(){
  var now = new Date();
  var nowyear = now.getFullYear();
  var nowmonth = now.getMonth()+1;
  var nowdate = now.getDate();
  var nowhours = now.getHours();
  var nowminites = now.getMinutes();
  var nowseconds = now.getSeconds();
  // var text = nowdate + " " + nowhours + ":" + nowminites + ":" + nowseconds;
  var text = nowyear + "年" + nowmonth + "月" +nowdate + "日" + nowhours + ":" + nowminites + ":" + nowseconds;
  return text;
}
