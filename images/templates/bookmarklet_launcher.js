(function(){
    if (window.myBookmarklet !== undefined){
        myBookmarklet(); // Here we used a function name which is not declared in main js file (bookmarklet.js) 
                        //so the bookmarklet runs everytime we click the if logic here is not working but we can 
                        // make it work by making the main function name myBookmarklet
    }
    else {
        document.body.appendChild(document.createElement('script')).
 src='https://127.0.0.1:8000/static/js/bookmarklet.js?r='+Math.
 floor(Math.random()*99999999999999999999);
    }
 })();