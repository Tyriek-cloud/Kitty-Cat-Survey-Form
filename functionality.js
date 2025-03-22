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

// Form submission logic with validation and AJAX
form.addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent default form submission (page reload)

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

    if (formValid) {
        // Create a FormData object to collect form data
        const formData = new FormData(event.target);

        // Send the form data to the Flask backend via AJAX (POST request)
        fetch('/submit', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            // After successful submission, fetch the average responses
            fetch('/average_responses')
                .then(response => response.json())
                .then(stats => {
                    // Display the statistics on the page
                    document.getElementById('average-age').innerText = stats.average_age || 'N/A';
                    document.getElementById('like-cats-count').innerText = stats.like_cats_count || 'N/A';
                    document.getElementById('most-popular-breed').innerText = stats.most_popular_breed || 'N/A';
                    
                    // Display disliked dog breeds
                    let dislikedBreeds = '';
                    for (let breed in stats.disliked_dogs) {
                        dislikedBreeds += `${breed}: ${stats.disliked_dogs[breed]}<br>`;
                    }
                    document.getElementById('disliked-dogs').innerHTML = dislikedBreeds || 'N/A';
                })
                .catch(error => {
                    console.error('Error fetching average responses:', error);
                });
        })
        .catch(error => {
            console.error('Error submitting form:', error);
        });
    }
});
