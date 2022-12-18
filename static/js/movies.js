// Toolip
// const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]')
// const tooltipList = [...tooltipTriggerList].map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl))

var tooltipTriggerLists = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
var tooltipLists = tooltipTriggerLists.map(function (tooltipTriggerEl) {
  return new bootstrap.Tooltip(tooltipTriggerEl)
})

// Slider
document.addEventListener('click',(e) => {
    let handle;
    if (e.target.matches('handle')) {
        handle = e.target
    }
    if (e.target.closest('.handle')) {
        handle = e.target.closest('.handle')
    }
    if(handle != null) {
        onHandleFunction(handle)
    }
})

const throttleProgressBar = throttle(()=> {

    document.querySelectorAll(".progress-bars").forEach(calculateProgressBar)
})

window.addEventListener('resize', throttleProgressBar)

document.querySelectorAll(".progress-bars").forEach(calculateProgressBar)

function calculateProgressBar(progressBar) {
    progressBar.innerHTML = ""
    const slider = progressBar.closest('.slider-cont').querySelector('.sliders')
    const itemCount = slider.children.length
    const itemsPerScreen = parseInt(getComputedStyle(slider).getPropertyValue('--items-per-screen'))
    let sliderIndex = parseInt(getComputedStyle(slider).getPropertyValue('--slider-index'))
    const progressBarItemCount = Math.ceil(itemCount / itemsPerScreen)

    if(sliderIndex >= progressBarItemCount) {
        slider.style.setProperty('--slider-index', progressBarItemCount - 1)
        sliderIndex = progressBarItemCount - 1
    }

    for (let i = 0; i < progressBarItemCount; i++) {
        const barItem = document.createElement('div')
        barItem.classList.add('progress-item')
        if (i === sliderIndex) {
            barItem.classList.add('active')
        }
        progressBar.append(barItem)
    }
}

function onHandleFunction(handle) {
    const progressBar = handle.closest('.slider-cont').querySelector('.progress-bars')
    const slider = handle.closest('.g-slider').querySelector('.sliders')
    let sliderIndex = parseInt(getComputedStyle(slider).getPropertyValue('--slider-index'))
    const progressBarCount = progressBar.children.length

    if (handle.classList.contains('left-handle')) {
        if(sliderIndex - 1 < 0) {  
            sliderIndex = progressBarCount - 1  
            slider.style.setProperty('--slider-index', sliderIndex)
            progressBar.children[0].classList.remove('active')
            progressBar.children[progressBarCount -1].classList.add('active')
        }else {
            slider.style.setProperty('--slider-index', sliderIndex - 1)

            progressBar.children[sliderIndex].classList.remove('active')
            progressBar.children[sliderIndex - 1].classList.add('active')
        }
    }

    if (handle.classList.contains('right-handle')) {
        if (sliderIndex + 1 >= progressBarCount) {
            slider.style.setProperty('--slider-index',0)
            progressBar.children[sliderIndex].classList.remove('active')
            progressBar.children[0].classList.add('active')
        } else {
            slider.style.setProperty('--slider-index', sliderIndex + 1)
            progressBar.children[sliderIndex].classList.remove('active')
            progressBar.children[sliderIndex + 1].classList.add('active')
        }
    }

    
}

function throttle(cb, delay = 1000) {
    let shouldWait = false
    let waitingArgs
    const timeoutFunc = () => {
      if (waitingArgs == null) {
        shouldWait = false
      } else {
        cb(...waitingArgs)
        waitingArgs = null
        setTimeout(timeoutFunc, delay)
      }
    }
  
    return (...args) => {
      if (shouldWait) {
        waitingArgs = args
        return
      }
  
      cb(...args)
      shouldWait = true
      setTimeout(timeoutFunc, delay)
    }
  }


// Home page 
const b_all = document.getElementById('b_all')
const b_movies = document.getElementById('b_movies')
const b_tv = document.getElementById('b_tv')
let t_all = document.getElementById('t_all')
let t_movies = document.getElementById('t_movies')
let t_tv = document.getElementById('t_tv')

b_all.addEventListener('click',()=> {
    t_all.style.display = 'flex'
    t_movies.style.display = 'none'
    t_tv.style.display = 'none'
})

b_movies.addEventListener('click',()=> {
    t_all.style.display = 'none'
    t_movies.style.display = 'flex'
    t_tv.style.display = 'none'
})

b_tv.addEventListener('click',()=> {
    t_all.style.display = 'none'
    t_movies.style.display = 'none'
    t_tv.style.display = 'flex'
})