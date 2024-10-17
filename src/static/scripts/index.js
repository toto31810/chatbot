const openButton = document.querySelector('button#chatbot-toggle')
const form = document.querySelector('#chatbot-form')

function openChatbot() {
	console.log('chatbot opened.')
}

async function handleForm(event) {
	event.preventDefault()
}

document.addEventListener('DOMContentLoaded', async () => {
	openButton.addEventListener('click', openChatbot)
	form.addEventListener('submit', handleForm)

	const commonQuestions = await fetch('/api/questions/common')
		.then((response) => response.json())

	console.log(commonQuestions)
})
