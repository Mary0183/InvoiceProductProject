const deleteLinks = document.querySelectorAll('.delete_link')

for (const deleteLink of deleteLinks) {
    deleteLink.addEventListener('click', function (event) {
        
        if (!confirm('are you sure you want to delete?')) {
            event.preventDefault()
        } 
    })
}