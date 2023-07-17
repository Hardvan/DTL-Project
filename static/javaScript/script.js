//Carousel Type 1

let counter = 0;
let rCounter = 2;

function advance() {
  const sources = [
    "https://i.ibb.co/8XjGdqG/urhack.jpg",
    "https://i.ibb.co/M6kVLxG/spark.jpg",
    "https://i.ibb.co/16hc92Y/esumit.jpg",
    "https://i.ibb.co/ykRbtKR/8thMile.jpg",
    "https://i.ibb.co/gjpCPTP/fest.jpg",
    "https://i.ibb.co/nBSM2Z1/marathon.jpg",
  ];
  document.getElementById("img1").src = document.getElementById("img2").src;
  document.getElementById("img2").src = document.getElementById("img3").src;
  document.getElementById("img3").src = sources[counter];
  counter++;
  rCounter++;
  if (counter === 6) {
    counter = 0;
    rCounter = 2;
  }
  if (rCounter === 6) {
    rCounter = 0;
  }
}

function retreat() {
  const sources = [
    "https://i.ibb.co/8XjGdqG/urhack.jpg",
    "https://i.ibb.co/M6kVLxG/spark.jpg",
    "https://i.ibb.co/16hc92Y/esumit.jpg",
    "https://i.ibb.co/ykRbtKR/8thMile.jpg",
    "https://i.ibb.co/gjpCPTP/fest.jpg",
    "https://i.ibb.co/nBSM2Z1/marathon.jpg",
  ];
  document.getElementById("img3").src = document.getElementById("img2").src;
  document.getElementById("img2").src = document.getElementById("img1").src;
  document.getElementById("img1").src = sources[rCounter];
  rCounter--;
  counter--;
  if (rCounter === -1) {
    rCounter = 5;
    counter = 3;
  }
  if (counter === -1) {
    counter = 5;
  }
}

//Carousel Type 2

let counter_2 = 0;
let rCounter_2 = 2;

function advance_2() {
  const sources = [
    "https://i.ibb.co/8XjGdqG/urhack.jpg",
    "https://i.ibb.co/M6kVLxG/spark.jpg",
    "https://i.ibb.co/16hc92Y/esumit.jpg",
    "https://i.ibb.co/ykRbtKR/8thMile.jpg",
    "https://i.ibb.co/gjpCPTP/fest.jpg",
    "https://i.ibb.co/nBSM2Z1/marathon.jpg",
  ];
  document.getElementById("img1_2").src = document.getElementById("img2_2").src;
  document.getElementById("img2_2").src = document.getElementById("img3_2").src;
  document.getElementById("img3_2").src = sources[counter_2];
  counter_2++;
  rCounter_2++;
  if (counter_2 === 6) {
    counter_2 = 0;
    rCounter_2 = 2;
  }
  if (rCounter_2 === 6) {
    rCounter_2 = 0;
  }
}

function retreat_2() {
  const sources = [
    "https://i.ibb.co/8XjGdqG/urhack.jpg",
    "https://i.ibb.co/M6kVLxG/spark.jpg",
    "https://i.ibb.co/16hc92Y/esumit.jpg",
    "https://i.ibb.co/ykRbtKR/8thMile.jpg",
    "https://i.ibb.co/gjpCPTP/fest.jpg",
    "https://i.ibb.co/nBSM2Z1/marathon.jpg",
  ];
  document.getElementById("img3_2").src = document.getElementById("img2_2").src;
  document.getElementById("img2_2").src = document.getElementById("img1_2").src;
  document.getElementById("img1_2").src = sources[rCounter_2];
  rCounter_2--;
  counter_2--;
  if (rCounter_2 === -1) {
    rCounter_2 = 5;
    counter_2 = 3;
  }
  if (counter_2 === -1) {
    counter_2 = 5;
  }
}

//Carousel Type 3

let counter_3 = 0;

function playback() {
  setInterval("playback_for_real();", 5000);
}

function playback_for_real() {
  const sources = [
    "https://i.ibb.co/8XjGdqG/urhack.jpg",
    "https://i.ibb.co/M6kVLxG/spark.jpg",
    "https://i.ibb.co/16hc92Y/esumit.jpg",
    "https://i.ibb.co/ykRbtKR/8thMile.jpg",
    "https://i.ibb.co/gjpCPTP/fest.jpg",
    "https://i.ibb.co/nBSM2Z1/marathon.jpg",
  ];
  document.getElementById("img1_3").src = document.getElementById("img2_3").src;
  document.getElementById("img2_3").src = document.getElementById("img3_3").src;
  document.getElementById("img3_3").src = sources[counter_3];
  counter_3++;
  if (counter_3 === 6) {
    counter_3 = 0;
  }
}
