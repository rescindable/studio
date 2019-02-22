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
		fromtime: null,
		totime: null,
	},
	methods: {
		checkForm: function(e) {
			if (this.name && this.fromtime && this.totime) {
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
