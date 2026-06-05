window.addEventListener('scroll', () => {

const navbar = document.querySelector('.navbar');

if(window.scrollY > 50){

navbar.style.background =
'rgba(3,13,18,.92)';

}else{

navbar.style.background =
'rgba(3,13,18,.75)';

}

});

window.addEventListener('load',()=>{

document.body.style.opacity='1';

});