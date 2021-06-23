

let images = ["https://vetstreet-brightspot.s3.amazonaws.com/75/78/5aaf3e0f424f93f9c30573125045/woman-and-cat-eskimo-kiss-thinkstock-78405666.jpg",
                  "https://i.insider.com/5afc93865e48ec51008b458a?width=600&format=jpeg&auto=webp",
                  "https://allaboutcats.com/wp-content/uploads/2017/04/cats-and-old-people2.jpg",
                  "https://todaysveterinarynurse.com/wp-content/uploads/sites/3/2019/07/HomelessKitten_shutterstock_44573680_forestpath.jpg",
                  "https://www.cdc.gov/healthypets/images/pets/woman-with-cat-asleep-medium.jpg",
                  "https://bloximages.newyork1.vip.townnews.com/greensboro.com/content/tncms/assets/v3/editorial/0/36/036951da-7d85-5e58-94ae-db85392c0bc6/5e8540d313e3e.image.jpg?resize=1200%2C800",
                  "https://images2.minutemediacdn.com/image/upload/c_fit,f_auto,fl_lossy,q_auto,w_728/v1555991808/shape/mentalfloss/istock_28625938_small_0.jpg?itok=m_cQ0h0i",
                  "https://www.declawing.com/images/benefits_of_cats_for_elderly_people.jpg",
                  "https://qph.fs.quoracdn.net/main-qimg-2eac95e0565e3c3575ca4d672b017555.webp",
                  "https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fstatic.onecms.io%2Fwp-content%2Fuploads%2Fsites%2F20%2F2020%2F06%2F22%2Fmen-cats-dating-1.jpg&q=85",
                  "https://www.petmd.com/sites/default/files/girl-holding-her-cat-picture-id854219324.jpg",
                  "https://www.rd.com/wp-content/uploads/2021/01/GettyImages-1272014800-e1610567180363.jpg",
                  "https://img-s3.onedio.com/id-57fe360b546101d10dc01835/rev-0/raw/s-a2e60d6870e46755e2804dcaf069d2ae60881205.jpg",
                  "https://www.arl-iowa.org/webres/Image/News/catandbaby.jpg"
                ];

   let imgSrc = document.getElementById('shiftImg');
   let idx = 0;
  function changeImg() {
    imgSrc.src = images[idx];
    
    // idx = Math.floor(Math.random()* images.length); // should use with +25 images
    idx++;
    if (idx >= images.length) {
      idx = 0;
    }
  }
  // issue with set interval on chrome speeds the intervals
setInterval(changeImg, 12000);
