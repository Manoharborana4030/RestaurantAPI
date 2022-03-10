// console.log('Generators')
// To genrate value on the fly


// function* gen(){
// 	for(let i = 1; i<3; i++){
// 		yield i
// 	}
// }

// const mygen = gen()
// console.log(mygen.next())
// console.log(mygen.next())



// ---------------Fetch

// let url = 'http://api.openweathermap.org/data/2.5/weather?q=ahmedabad&units=metric&appid=3e1f28d5af278806ac12cef05d19752e'
// fetch(url)
// .then(res => res.json())
// .then(data => console.log("Whether Details:",data['main']))




// -------------------------------------------draw program


// function draw(no) {
//             let random_no = Math.floor(Math.random() * 3);
//             let check = new Promise((same,different) => {
//                 if (random_no == no) {
//                     same("Congratulation you won the money, announce no. was also: "+random_no );
//                 } else {
//                     different("Better luck next time, announce no was :"+random_no);
//                 }
//             });
//             return check;
//         }

// function result() {
//             let l_no = document.getElementById("no").value;
//             draw(l_no)
//                 .then((announcement) => {
//                     console.log(announcement);
//                 })
//                 .catch((announcement) => {
//                     console.log(announcement);
//                 });

//         }


// #-----------------------------------------------


class Student { 

    constructor(name, enrollment, std) { 

      this.name = name; 

      this.enrollment =  enrollment; 

      this.std = std; 

    } 

    StudentDetails(){ 

        return (`name: ${this.name} ,enrollment: ${this.enrollment}, standard: ${this.std} `) 

    } 

  } 

  let rahul = new Student('rahul', 101, 10); 

  let manohar = new Student('Manohar', 102, 11); 

  console.log(rahul.name);     

  console.log(rahul.std);   

  console.log(manohar.StudentDetails()); 