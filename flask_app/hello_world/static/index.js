window.onload = init;

function init(){
    console.log('javascript is loaded');
    wrapperFunction(saySomething);
}

function saySomething(){
    console.log("something")
}

function wrapperFunction(callback){
    
    console.log("wrapper stuff")
    callback();
}

