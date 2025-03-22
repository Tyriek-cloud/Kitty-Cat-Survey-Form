// Get form elements
const form = document.getElementById("survey-form");
const nameInput = document.getElementById("name");
const emailInput = document.getElementById("email");
const ageInput = document.getElementById("age");
const likeCatsSelect = document.getElementById("like-cats");
const ownCatsSelect = document.getElementById("own-cats");
const favoriteActivitySelect = document.getElementById("favorite-activity");
const favoriteActivityLabel = document.getElementById("favorite-activity-label");

// Show favorite activity field if the user owns cats
ownCatsSelect.addEventListener('change', function() {
    if (ownCatsSelect.value === "Yes. Good answer.") {
        favoriteActivityLabel.style.display = "block";
        favoriteActivitySelect.style.display = "block";
    } else {
        favoriteActivityLabel.style.display = "none";
        favoriteActivitySelect.style.display = "none";
    }
});

// Form validation before submission
form.addEventListener('submit', function(event) {
    let formValid = true;

    // Simple email validation
    const emailRegex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;
    if (!emailRegex.test(emailInput.value)) {
        alert("Please enter a valid email address.");
        formValid = false;
    }

    // Check age if entered (optional field)
    if (ageInput.value && (ageInput.value < 10 || ageInput.value > 100)) {
        alert("Please enter a valid age between 10 and 100.");
        formValid = false;
    }

    if (!formValid) {
        event.preventDefault(); // Prevent form submission if validation fails
    } else {
        alert("Survey submitted successfully!");
    }
});
