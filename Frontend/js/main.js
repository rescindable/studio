var app = new Vue({
	el: '#body',
	data: {
		message: "This is Vue"
	},
	methods: {
		reverseMessage: function() {
			this.message = this.message.split('').reverse().join('');
		}
	}
});

var form = new Vue({
	el: '#submissionForm',
	data: {
		errors: [],
		name: null,
		from-time: null,
		to-time: null,
	},
	methods: {
		checkForm: function(e) {
			if (this.name && this.from-time && this.to-time) {
				return true;
			}
			this.errors = [];
			if (!this.name) {
				this.errors.push("We'll need your name");
			}
			e.preventDefault();
		}
	}
})
