const htmlbody = document.querySelector('body');

const clickfunction = function(){
    const colors=['red', 'blue', 'purple', 'green'];
    const randomIndex = Math.floor(Math.random() * colors.length );
    const randomColor = colors[randomIndex];
    htmlbody.style.backgroundColor = randomColor;
}
