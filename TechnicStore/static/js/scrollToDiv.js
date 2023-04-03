function scrollToMyDiv(btn) {
    const active = document.querySelector('.active-tab-0-2-380');
  
    active.classList.remove('active-tab-0-2-380');
    active.classList.add('active-tab-0-2-381');
    btn.classList.remove('active-tab-0-2-381');
    btn.classList.add('active-tab-0-2-380');
    const elem = document.getElementById('details');
    const header = document.getElementById('header');
    const height = header.clientHeight;
    const rect = elem.getBoundingClientRect();
    const distanceToTop = rect.top;
    window.scrollBy(0, distanceToTop - (height + 20));
}

function leaveBottom() {
    const active = document.querySelector('.active-tab-0-2-380');

    const id1 = document.getElementById('id1');
    id1.style.width = `${Math.round(active.getBoundingClientRect().width)}px`;

    const styles = window.getComputedStyle(active);
    const leftPadding = parseInt(styles.getPropertyValue('padding-left'));

    const container = document.getElementById('container_for_padding');
    const leftContain = container.getBoundingClientRect().left

    id1.style.left = `${Math.round(active.getBoundingClientRect().left - Math.round(leftPadding) - Math.round(leftContain) + 3)}px`;
}

function replaceBottom(btn) { 
    const id1 = document.getElementById('id1');
    
    id1.style.width = `${Math.round(btn.getBoundingClientRect().width)}px`;

    const styles = window.getComputedStyle(btn);
    const leftPadding = parseInt(styles.getPropertyValue('padding-left'));

    const container = document.getElementById('container_for_padding');
    const leftContain = container.getBoundingClientRect().left

    id1.style.left = `${Math.round(btn.getBoundingClientRect().left - Math.round(leftPadding) - Math.round(leftContain) + 3)}px`;
}