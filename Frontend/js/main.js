var app = new Vue({
	el: '#pageWrapper',
	data: {
		message: "This is Vue"
	},
	methods: {
		reverseMessage: function() {
			this.message = this.message.split('').reverse().join('')
		}
		bookSlot: function() {
			// Get info from
			// Send POST here
			
		}
	}
});
