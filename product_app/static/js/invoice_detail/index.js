// Selecciona el elemento del html que tiene el id #select_product y lo asigna a la variable
const selectList=document.querySelector('#select_product')

// Selecciona el elemento del html que tiene el id #price y lo asigna a la variable
const priceField=document.querySelector('#price')

// Selecciona el elemento del html que tiene el id #quantity y lo asigna a la variable
const quantityField=document.querySelector('#quantity')

// Cada vez que eliges una opcion del dropdown se ejecuta este codigo
// event.target se refiere al select list donde paso el evento
// event.target.value es el valor que tomo el select list despues que seleccionaste una opcion
selectList.onchange=function(event){
    // La primera opcion (que esta vacia) tiene un valor "0"
    // Aqui chequeamos si esta fue la que elegiste y le ponemos el atributo "disabled" a los input fields de precio y cantidad
    if(event.target.value==='0'){
        priceField.disabled=true
        quantityField.disabled=true
    } else{
        priceField.disabled=false
        quantityField.disabled=false
    }
    console.log(event.target.value)
}

// Esto es parecido a lo del select, lo unico que el evento se ejecuta cada vez que escribes
priceField.oninput=function(event){
      // aqui validamos si el valor que tiene el field es un "Not a Number"
    if(isNaN(event.target.value)){
    // si es un "Not a Number, es decir no es un numero, tiramos un warning"
        alert('only numbers please')
    }

}

// Lo mismo del anterior
quantityField.oninput=function(event){
    if(isNaN(event.target.value)){
        alert('only numbers please')
    }

}
