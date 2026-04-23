// Basic JavaScript script for posts.js

// Example data
const posts = [
    {
        'title': 'Post 1',
        'content': 'This is the content of post 1.',
        'author': 'Author 1'
    },
    {
        'title': 'Post 2',
        'content': 'This is the content of post 2.'
    }
];

// Render posts into a container with id="posts"
function renderPosts() {
    const container = document.getElementById("posts");
    if (!container) {
        console.warn("No element with id 'posts' found.");
        return;
    }

    container.innerHTML = "";

    posts.forEach(post => {
        const postItem = document.createElement("div");
        postItem.className = "post";

        const title = document.createElement("h2");
        title.textContent = post.title;

        const content = document.createElement("p");
        content.textContent = post.content;

        postItem.appendChild(title);
        postItem.appendChild(content);
        container.appendChild(postItem);
    });
}

// Add a new post
function addPost(title, content) {
    const newPost = {
        id: posts.length + 1,
        title,
        content
    };
    posts.push(newPost);
    renderPosts();
}

// Initialize when DOM is ready
document.addEventListener("DOMContentLoaded", () => {
    renderPosts();
});