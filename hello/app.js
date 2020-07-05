// note that the fs package does not exist on a normal browser
const fs = require("fs");
const { Console } = require("console");
//a dialog box module from electron
const { dialog } = require("electron").remote;
// Also note that document does not exist in a normal node environment
// button click event
document.getElementById("myButton").addEventListener("click", () => {
    const msg = "Button Clicked!!!";  // the data we want to save to the desktop  
    heading = document.getElementById("myHeading");
    heading.innerHTML = msg
    console.log(msg);
});