// AQUI COMIENZO CON LO DE PYTHON

const PORT = 5001;
const DOMAIN = "http://localhost:"
const RESOURCE = "main"
const POST_ROUTE = "post_endpoint"

const getMain = async () => {
    try {
        const raw = await fetch(`${DOMAIN}${PORT}/${RESOURCE}`)
        const response = await raw.json()
        displayResults(response)
    } catch (error) {
        console.log(error, 'efe');
    }
}

const postEndpoint = async () => {
    try {
        const raw = await fetch(`${DOMAIN}${PORT}/${POST_ROUTE}`, {
            method : 'POST', 
            headers : {
                'Content-Type' : 'application/json'
            },
            body : JSON.stringify({'name':'Sarha'})
        })
        const response = await raw.json()
        console.log(response);
    } catch (error) {
        console.log(error);
    }
}


// creando los elementos del DOM
const food_types = document.querySelectorAll('.food_item');
const cal_slide = document.getElementById('calorias_slide')
const fat_slide = document.getElementById('grasa_slide')
const carb_slide = document.getElementById('carbohidratos_slide')
const fib_slide = document.getElementById('fibra_slide')
const prot_slide = document.getElementById('proteina_slide')
const btn_step1 = document.getElementById('step_1_next');
const btn_protomeal = document.getElementById('step_2_next')

var knn_section = document.getElementById('knn_section')

// variables globales
var selected_food = [];
var slide_arr = [];

// Metodos
const displayResults = (namesList) => {
    knn_section.innerHTML = ''
    namesList.forEach(i =>{
        const node = document.createElement('h4')
        const text = document.createTextNode(i)
        node.appendChild(text)
        document.getElementById('knn_section').appendChild(node)
    })
}

// Event listener para cada item de la pantalla 1
food_types.forEach(item => {
    item.addEventListener('click', () => {
        if(item.classList.contains('selected')){
            item.classList.remove('selected');
            selected_food.splice(item.getAttribute('id'),1)
            //console.log(selected_food);
        }else{
            item.classList.add('selected');
            selected_food.push(item.getAttribute('id'))
            //console.log(selected_food);
        }
    })
})

// Event listener para la pantalla 2. 
// slide_arr es el elemento que hay que enviar a main.py
btn_protomeal.addEventListener('click', (e)=>{
    slide_arr=[];
    slide_arr.push(cal_slide.value, fat_slide.value, carb_slide.value, fib_slide.value, prot_slide.value);
    var temp = [0,0,0,0,0,0,0];
    selected_food.forEach( i => {
        if (i == "bak"){
            temp[0]=1
        }else if (i == "bow"){
            temp[1] = 1
        }else if (i == "hbf"){
            temp[2] = 1
        }else if (i == "swe"){
            temp[3] = 1
            temp[6] = 1
        }else if (i == "sdw"){
            temp[4] = 1
        }else if (i == "sal"){
            temp[4] = 1
        }
    ;})
    temp.forEach(i => {
        slide_arr.push(i)
    })
    //postEndpoint();
    getMain();
    //console.log(slide_arr);
})

//postEndpoint();