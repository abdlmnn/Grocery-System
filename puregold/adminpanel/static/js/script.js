
// ====New Sidebar Menu====
class MenuBar{
    constructor(){
        this.sidebar = document.getElementById('sidebar-modal');
        this.resizeClose();
        this.outsideClick();
    }

    openSide(){
        return this.sidebar.style.height = '100%';
    }

    closeSide(){
        return this.sidebar.style.height = '0';
    }

    resizeClose(){
        window.addEventListener('resize', ()=>{
            if(this.sidebar.style.height === '100%'){
                this.closeSide();
            }
        })
    }

    outsideClick(){
        document.addEventListener('click', (event) => {
            const isClickInside = this.sidebar.contains(event.target);
            const isToggleButton = event.target.closest('button')?.onclick?.toString().includes("openSide");
            
            if (!isClickInside && !isToggleButton && this.sidebar.style.height === '100%') {
                this.closeSide();
            }
        });
    }
}

// ====Notification Dropdown====
class Notification{
    constructor(){
        this.dropdown = document.getElementById('dropdown-Notification');
        this.button = document.querySelector('.notification-btn-header');
        this.closeNotif();
        this.outsideClick();
    }

    openNotif(){
        this.dropdown.classList.toggle('active');
        this.button.classList.toggle('active-notification');
    }

    closeNotif(){
        this.dropdown.classList.remove('active');
        this.button.classList.remove('active-notification');
    }

    outsideClick() {
        document.addEventListener('click', (e) => {
            const isClickInside = this.dropdown.contains(e.target) || this.button.contains(e.target);

            if (!isClickInside) {
                this.closeNotif();
            }
        });
    }
}

const menuBar = new MenuBar();
const notification = new Notification();

// ====Sidebar Dropdown====
const dropdown = document.getElementsByClassName('dropdown-btn');
var i;
for(i=0; i<dropdown.length; i++){
    dropdown[i].addEventListener('click',function(){

        this.classList.toggle('active');

        for(let j = 0; j < dropdown.length; j++){
            if(dropdown[j] !== this){
                dropdown[j].classList.remove('active');
                dropdown[j].nextElementSibling.style.display = 'none';
            }
        }

        var dropdownContent = this.nextElementSibling;

        if(dropdownContent.style.display === 'flex'){
            dropdownContent.style.display = 'none';
        }else{
            dropdownContent.style.display = 'flex'
        }

        var selected = dropdownContent.querySelector('.selected')

        if(this.classList.contains('active')){
            if(selected){
                selected.classList.add('active');
            }
        }else{
            if(selected){
                selected.classList.remove('active');
            }
        }
    })
}