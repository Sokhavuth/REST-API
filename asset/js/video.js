//asset/js/vedeo.js

function setIframe(type, id){
    
    if(type == "YouTube"){
        $('#player').attr("src","https://www.youtube.com/embed/"+id)
    }else if(type == "YouTubePlaylist"){
        $('#player').attr("src","https://www.youtube.com/embed/videoseries?list="+id)
    }else if(type == "Facebook"){
        $('.fb-video').attr("data-href","https://www.facebook.com/video.php?v="+id)
    } 

}