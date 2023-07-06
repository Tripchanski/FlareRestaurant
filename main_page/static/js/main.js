

(function () {
    function scrollHorizontally(e) {
        e = window.event || e;
        var delta = Math.max(-1, Math.min(1, (e.wheelDelta || -e.detail)));
        document.getElementById('all_contacts').scrollLeft -= (delta * 50); // Multiplied by 40
        e.preventDefault();
    }
    if (document.getElementById('all_contacts').addEventListener) {
        // IE9, Chrome, Safari, Opera
        document.getElementById('all_contacts').addEventListener("mousewheel", scrollHorizontally, false);
        // Firefox
        document.getElementById('all_contacts').addEventListener("DOMMouseScroll", scrollHorizontally, false);
    } else {
        // IE 6/7/8
        document.getElementById('all_contacts').attachEvent("onmousewheel", scrollHorizontally);
    }
})();