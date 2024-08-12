let statut = document.querySelector('#status')
let option = document.querySelectorAll('option')
let box = document.querySelectorAll('.box')
let search = document.querySelector('.search')
let span = document.querySelector('#count-element')
let container = document.querySelector('.container')
let current_element = 0
let count = 0 



statut.addEventListener('change' , function(){
   console.log(statut.value)
})

const typed = new Typed('#logo', {
    strings : ['Alae Lahbichi'] , 
    typeSpeed: 50 ,
    backSpeed : 50 , 
    backDelay : 1500 , 
    loop : true ,
}) ;
 
container.querySelectorAll('.box').forEach((e)=>{
    current_element++
})

console.log(current_element)

span.textContent = "("+current_element+")"
search.addEventListener('keyup',function(){
    box.forEach((e)=>{
        if(e.querySelector('h2').textContent.includes(search.value)){
            e.style.display="flex"
            count ++ 
            current_element = count
        }else {
            e.style.display="none"
            current_element = count
        }
    })
    span.textContent = "("+current_element+")"
    count = 0 ; 
})



