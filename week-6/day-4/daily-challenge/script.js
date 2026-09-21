const playerSubForm = document.querySelector("#player-sub-form");

function submitGuess(guess) {
    fetch('/guess', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ guess: guess })
    })
        .then((response) => response.json())
        .then((data) => {
            const feedback = document.querySelector('#feedback');
            const scoreDisplay = document.querySelector('#score-display');

            if (data.correct) {
                feedback.textContent = 'Correct!';
                scoreDisplay.textContent = `Score: ${data.score}`;
            } else {
                feedback.textContent = `Wrong! It was ${data.answer}`;
            }

            fetch('/round')
                .then((response) => response.json())
                .then((data) => {
                    document.querySelector('#emoji-display').textContent = data.emoji;

                    const optionsContainer = document.querySelector('#options-container');
                    optionsContainer.innerHTML = '';

                    data.options.forEach((option) => {
                        const button = document.createElement('button');
                        button.textContent = option.name;
                        button.addEventListener('click', () => {
                            submitGuess(option.name);
                        });
                        optionsContainer.appendChild(button);
                    });
                });
        });
}

playerSubForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const newPlayerInput = document.querySelector("#new-player-name");
    const newPlayerName = newPlayerInput.value;

    fetch('/newPlayerEntry', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name: newPlayerName })
    }).then(() => {
        fetch('/round')
            .then((response) => response.json())
            .then((data) => {
                document.querySelector('#emoji-display').textContent = data.emoji;
                const optionsContainer = document.querySelector('#options-container');
                optionsContainer.innerHTML = '';
                data.options.forEach((option) => {
                    const button = document.createElement('button');
                    button.textContent = option.name;
                    button.addEventListener('click', () => {
                        submitGuess(option.name);
                    });
                    optionsContainer.appendChild(button);
                });
            });
    });
});