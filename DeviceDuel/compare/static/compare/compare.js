const phoneBtn = document.getElementById("SmartPhones");
const productContainers = [...document.querySelectorAll('.product-container')];
const nxtBtn = [...document.querySelectorAll('.nxt-btn')];
const preBtn = [...document.querySelectorAll('.pre-btn')];

const compareBtn = document.getElementsByClassName("login-btn")



productContainers.forEach((item, i) => {
    let containerDimensions = item.getBoundingClientRect();
    let containerWidth = containerDimensions.width;

    nxtBtn[i].addEventListener('click', () => {
        item.scrollLeft += containerWidth;
    })

    preBtn[i].addEventListener('click', () => {
        item.scrollLeft -= containerWidth;
    })
})

buttons = document.getElementsByClassName("card-btn")
console.log(buttons)
let id_list = new Array()

function changeText(btn) {
    if (btn.innerText === "Select") {
        if (id_list.length < 3) {
            btn.innerText = "Selected";
            btn.classList.add("selected");
            id_list.push(btn.id)
        } else {
            alert("You Can not select more than 3 Devices")
        }
    } else {
        btn.innerText = "Select";
        btn.classList.remove("selected");
        let index = id_list.indexOf(btn.id)
        id_list.splice(index, 1)

    }
    console.log(id_list)
}

Array.from(compareBtn).forEach((btn) => {
    btn.addEventListener('click', function () {
        const dataToSend = {
            [btn.id]: id_list
        };
        axios.post("/compare_selected/", dataToSend, {
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": getCookie("csrftoken")
            }
        }).then(response => {
            const redirectUrl = response.data.redirect_url
            window.location.href = redirectUrl

        })
            .catch(error => {
                console.error("Compare failed:", error);
            });
    });
})



// phoneBtn.addEventListener("click", sendDataToDjango)





