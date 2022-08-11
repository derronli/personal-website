//Plays css animation a single time per session 

//listens for loading event and stores displayed value to the session
window.addEventListener(('load'), () => {
    if(document.querySelector('#navbar') !== null) {
   window.sessionStorage.setItem('Heading', 'displayed');
   }
   })
//if displayed value is stored, remove animation class from HTML element
if (window.sessionStorage.getItem('Heading')) {
    document.querySelector('#navbar').classList.remove("bar");
}
