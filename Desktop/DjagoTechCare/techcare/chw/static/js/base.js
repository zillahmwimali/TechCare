const side = document.querySelector('.side');
const sideWrapper = document.querySelector('.side-wrapper');
const xBtn = document.querySelector('.side-header i');
const toggle = document.querySelector('.toggle');
const circle = document.querySelector('.circle');
const user = document.querySelector('.user');




// use profile
user.addEventListener('click', () => {
	side.classList.add('side-display');
	sideWrapper.classList.add('side-wrapper-display');
});

xBtn.addEventListener('click', () => {
	side.classList.remove('side-display');
	sideWrapper.classList.remove('side-wrapper-display');
});

// dark mode
const darkElements1 = document.querySelectorAll('.dark-mode-1');
const darkElements2 = document.querySelectorAll('.dark-mode-2');
const lighTexts = document.querySelectorAll('.light-text');
const borders = document.querySelectorAll('.border');

toggle.addEventListener('click', () => {
	circle.classList.toggle('move');
	Array.from(darkElements1).map(darkEl1 => darkEl1.classList.toggle('dark-1'));
	Array.from(darkElements2).map(darkEl2 => darkEl2.classList.toggle('dark-2'));
	Array.from(lighTexts).map(lighText => lighText.classList.toggle('light'));
	Array.from(borders).map(border => border.classList.toggle('border-color'));
});