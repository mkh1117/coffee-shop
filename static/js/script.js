const searchBtn = document.getElementById('search-btn');
const searchForm = document.querySelector('.search-form');

if(searchBtn){
    searchBtn.addEventListener('click', () => {
        searchForm.classList.toggle('active');
    });
}

const modal = document.getElementById("modal");
const openBtn = document.getElementById("openModalBtn");
const closeBtn = document.getElementById("closeModalBtn");

if(openBtn){
    openBtn.onclick = () => {
        modal.classList.add("active");
    }
}

if(closeBtn){
    closeBtn.onclick = () => {
        modal.classList.remove("active");
    }
}

window.onclick = (e) => {
    if(e.target === modal){
        modal.classList.remove("active");
    }
}

const signUpButton = document.getElementById('signUp');
const signInButton = document.getElementById('signIn');
const container = document.getElementById('container');

if(signUpButton){
    signUpButton.addEventListener('click', () => {
        container.classList.add("right-panel-active");
    });
}

if(signInButton){
    signInButton.addEventListener('click', () => {
        container.classList.remove("right-panel-active");
    });
}