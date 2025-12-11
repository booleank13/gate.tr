document.addEventListener('DOMContentLoaded', () => {
    const closeBtn = document.getElementById('closeBtn');

    closeBtn.addEventListener('click', () => {
        // In a real ad environment (e.g., Google Ad Manager), this would close the ad.
        // For this demo, we'll fade out the container.
        const container = document.querySelector('.ad-container');
        container.style.transition = 'opacity 0.5s';
        container.style.opacity = '0';

        setTimeout(() => {
            // Optional: Remove from DOM or reset
            // container.style.display = 'none';
            console.log('Ad closed');

            // Just for demo purposes, reload/reset after a few seconds so it can be seen again
            /*
            setTimeout(() => {
                container.style.opacity = '1';
            }, 1000);
            */
        }, 500);
    });
});
