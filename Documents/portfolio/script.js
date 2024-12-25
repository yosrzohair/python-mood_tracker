// Alert every 10 seconds
setInterval(() => {
    const userResponse = confirm("Do you need any support? Click 'OK' to go to the Contact Me section.");
    if (userResponse) {
      scrollToContact();
    }
  },10000 ); 


  function scrollToContact() {
    const contactSection = document.getElementById("contact");
    if (contactSection) {
      contactSection.scrollIntoView({ behavior: "smooth" });
    }
  }
  