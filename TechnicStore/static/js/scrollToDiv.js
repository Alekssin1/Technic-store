function scrollToMyDiv() {
    const elem = document.getElementById('details');
    const header = document.getElementById('header');
    const height = header.clientHeight;
    const rect = elem.getBoundingClientRect();
    const distanceToTop = rect.top;
    window.scrollBy(0, distanceToTop - (height + 20));

}