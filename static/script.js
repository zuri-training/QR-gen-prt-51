function togglePassword() {
        let pswd = document.getElementById("password");
        if (pswd.getAttribute("type") === "password") {
          pswd.setAttribute("type", "text");
          document
            .getElementById("toggle")
            .setAttribute("class", "fa fa-eye-slash");
        } else {
          pswd.setAttribute("type", "password");
          document.getElementById("toggle").setAttribute("class", "fa fa-eye");
        }
      }

function togglePassword1() {
        let pswd = document.getElementById("password1");
        if (pswd.getAttribute("type") === "password") {
          pswd.setAttribute("type", "text");
          document
            .getElementById("toggle")
            .setAttribute("class", "fa fa-eye-slash");
        } else {
          pswd.setAttribute("type", "password");
          document.getElementById("toggle").setAttribute("class", "fa fa-eye");
        }
      }
function togglePassword2() {
        let pswd = document.getElementById("password2");
        if (pswd.getAttribute("type") === "password") {
          pswd.setAttribute("type", "text");
          document
            .getElementById("toggle")
            .setAttribute("class", "fa fa-eye-slash");
        } else {
          pswd.setAttribute("type", "password");
          document.getElementById("toggle").setAttribute("class", "fa fa-eye");
        }
      }