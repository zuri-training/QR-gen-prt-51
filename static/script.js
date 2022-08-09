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

function confirmPassword() {
        let pswd = document.getElementById("cfm_password");
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
