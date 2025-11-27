/*burgermenu*/

const burger = document.querySelector("#burgermenu");
const kreuz = document.querySelector("#kreuz");
const navi = document.querySelector(".animation");
let hmenu=true;
function menu() {
    /* navi.classList.toggle("show"); */
    // Symbole wechseln
    if (hmenu) {
        /* burger.classList.add("display"); */
        navi.classList.add("show");// Menü einblenden
        burger.style.display = "none";
        kreuz.style.display = "block";
        hmenu=false;
    } else {
        navi.classList.remove("show");// Menü ausblenden
        burger.style.display = "block";
        kreuz.style.display = "none";
        hmenu=true;
    }
}

// Event-Listener für beide Symbole
burger.addEventListener("click", menu);
kreuz.addEventListener("click", menu); 

window.onresize = function(){
    if(window.innerWidth > 921){
        burger.style.display = "none";
        kreuz.style.display = "none";
    }else{
        navi.classList.remove("show");// Menü ausblenden
        burger.style.display = "block";
        kreuz.style.display = "none";
        hmenu=true;
    }
};
