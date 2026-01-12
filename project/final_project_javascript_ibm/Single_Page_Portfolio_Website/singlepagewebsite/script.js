function addRecommendation() {
  // Get the message of the new recommendation
  let recommendation = document.getElementById("new_recommendation");
  // If the user has left a recommendation, display a pop-up
  if (recommendation.value != null && recommendation.value.trim() != "") {
    console.log("New recommendation added");
    // set popup message and show it
    var popupHeading = document.querySelector('#popup h3');
    if (popupHeading) popupHeading.textContent = 'Recommendation added';
    showPopup(true);

    // Create a new 'recommendation' element and set its content to the user's message
    var element = document.createElement("div");
    element.setAttribute("class","recommendation");
    element.innerHTML = '<span>&#8220;</span>' + escapeHtml(recommendation.value.trim()) + '<span>&#8221;</span>';
    // Add this element to the end of the list of recommendations
    document.getElementById("all_recommendations").appendChild(element);

    // Reset the value of the textarea
    recommendation.value = "";

    // hide popup after 2 seconds
    setTimeout(function(){ showPopup(false); }, 2000);
  }
}

function showPopup(bool) {
  if (bool) {
    document.getElementById('popup').style.visibility = 'visible'
  } else {
    document.getElementById('popup').style.visibility = 'hidden'
  }
}

// small helper to escape HTML in user input
function escapeHtml(unsafe) {
  return unsafe
       .replace(/&/g, "&amp;")
       .replace(/</g, "&lt;")
       .replace(/>/g, "&gt;")
       .replace(/\"/g, "&quot;")
       .replace(/'/g, "&#039;");
}
