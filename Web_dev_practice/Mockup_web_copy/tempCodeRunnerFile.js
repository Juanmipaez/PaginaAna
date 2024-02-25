const htmlbody = document.querySelector('body');

const clickfunction = function(){
    const colors = ['red','blue','green','purple','yellow','orange','black','grey'];
    const randomIndex = Math.floor(Math.random() * colors.length);
    const randomColor = colors[randomIndex];
    htmlbody.style.backgroundColor = randomColor;
    
}