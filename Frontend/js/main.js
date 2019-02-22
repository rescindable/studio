// Main JS
function prevWeek() {
	console.log('prevWeek');
}

// Define components
Vue.component('btn-scroll-left', {
	data: function() {},
	template: '<button v-on:click="prevWeek();">Previous Week</button>'
})

// Define instance
var app = new Vue({
	el: '#body',
	mouned: function() {
		this.init();
	},
	methods: {
		init:function () {
			fetch('/skeleton').then(
			function(response) {
				return response;
			}).then(function(pageskeleton){
				document.getElementById('body').innerHTML = pageSkeleton;
			})
		}
	}
})
