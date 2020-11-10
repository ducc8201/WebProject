var updateBtns = document.getElementsByClassName('add-to-cart-btn');
var productId;
var action;
for(var i = 0 ; i < updateBtns.length;i++){
    updateBtns[i].addEventListener('click',function(){
           productId = this.dataset.product;
            action = this.dataset.action;
           console.log("productID:",productId,"action:",action)


    console.log('User:'+user);
    if(user == 'AnonymousUser'){
        console.log('User is not authenticated')

    }else{
        UpdateCart(productId,action);
    }
 });

}
function UpdateCart(productId,action){
    var url ='/update_item/'
    fetch(url,{
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({'productId':productId,'action':action})

    })
    .then((response) =>{
        return response.json();
    })
    .then((data) =>{
        location.reload()
    });

}