var updateBtns = document.getElementsByClassName('add-to-cart-btn');
for(var i = 0 ; i < updateBtns.length;i++){
    updateBtns[i].addEventListener('click',function(){
           var productId = this.dataset.product;
           var action = this.dataset.action;
           console.log("productID:",productId,"action:",action)

    });
    console.log('User:'+user);
    if(user == 'AnonymousUser'){
        console.log('User is not authenticated')

    }else{
        console.log('User is authenticated,sendding data..')
    }
}