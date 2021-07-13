<template>
  <div class="home">
    <h1 class="title"> Contacts Book</h1>
    <hr>
    <h2 class="subtitle">Add contact</h2>
    <div class="columns">
      <div class="column is-4 is-offset-4">
        <form v-on:submit.prevent="addContact">
          <div class="field">
            <label class="lable">First Name</label>
            <div class="control">
              <input class="input" type="text" placeholder="First Name" v-model="firstname">
            </div>
          </div>

          <div class="field">
            <label class="lable">Last Name</label>
            <div class="control">
              <input class="input" type="text" placeholder="Last Name" v-model="lastname">
            </div>
          </div>

          <div class="field">
            <label class="lable">Phone</label>
            <div class="control">
              <input class="input" type="text" placeholder="+420 xxx xxx xxx" v-model="mobile_phone">
            </div>
          </div>

          <div class="field">
            <label class="lable">Email</label>
            <div class="control">
              <input class="input" type="text" placeholder="test@test.com" v-model="email">
            </div>
          </div>

          <div class="field">
            <label class="lable">Department</label>
            <div class="control">
              <input class="input" type="text" placeholder="Managment" v-model="department">
            </div>
          </div>

          <div class="field">
            <div class="control_btn has-text-centered">
              <button class="button is-rounded is-link">Add contact</button>
            </div>
          </div>

        </form>
      </div>
    </div>
    
    <div class="columns">
      <div class="column">
        <h2 class="subtitle">List of contacts:</h2>
        <div class="field has-addons column is-half is-offset-one-quarter">
          <div class="control has-text-centered">
            <input class="input" type="text" placeholder="Search or Filter" v-model="search_term">
          </div>
          <div class="control">
            <a class="button is-info" v-on:click.prevent="getContactInfo">
              Search/Filter
            </a>
          </div>
        </div>
        <div class="cantact">
          <div class="card column is-half is-offset-one-quarter" v-for="contact in contacts" :key="contact.id">
            <div class="card-content">
              <li> First Name: {{contact.firstname}} </li>
              <li> Last Name: {{contact.lastname}} </li>
              <li> Phone: {{contact.mobile_phone}} </li>
              <li> Email: {{contact.email}} </li>
              <li> Department: {{contact.department}} </li>
            </div>
          </div>
        </div>
      </div>
    </div>

  </div>
</template>

<script>
// @ is an alias to /src
import axios from 'axios'


export default {
  name: 'Home',
  data () {
    return {
      contacts: [],
      firstname: '',
      lastname: '',
      mobile_phone: '',
      email: '',
      department: '',
      search_term: ''
    }
  },
  mounted () {
    this.getContact(),
    this.getContactInfo()
  },
  methods: {
    getContact() {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/contactbook/',
        auth: {
          username: 'admin',
          password: 'admin'
        }
      }).then(response => this.contacts = response.data)
    },
    addContact() {
      if (this.firstname) {
        axios({
          method: 'post',
          url: 'http://127.0.0.1:8000/contactbook/',
          data: {
            firstname: this.firstname,
            lastname: this.lastname,
            mobile_phone: this.mobile_phone,
            email: this.email,
            department: this.department
          },
          auth: {
          username: 'admin',
          password: 'admin'
          }
        }).then((response) => {
          let newContact = {
            'id': response.data.id,
            'firstname': response.data.firstname,
            'lastname': response.data.lastname,
            'mobile_phone': response.data.mobile_phone,
            'email': response.data.email,
            'department': response.data.department
          }

          this.contacts.push(newContact)
          this.firstname = '',
          this.lastname = '',
          this.mobile_phone = '',
          this.email = '',
          this.department = ''
        }).catch((error) => {
          console.log(error)
        })
      }
    },
    getContactInfo() {
      if (this.search_term) {
        axios({
          method: 'get',
          url: `http://127.0.0.1:8000/contactbook/?search=${this.search_term}`,
          auth: {
          username: 'admin',
          password: 'admin'
          }
        }).then((response) => {
          this.contacts = response.data,
          this.search_term = ''
        }).catch((error) => {
          console.log(error)
        })
      }
      else {
        this.getContact()
      }
    }
  }
}
</script>

<style lang="scss">
.select, select {
  width: 100%;
  height: 100%;
}

.subtitle {
  text-align: center;
}

.title {
  text-align: center;
}

.card {
  margin-bottom: 5px;
}

.done {
  opacity: 0.3;
}

.field {
  margin-top: -0.4rem;
}

.title {
  margin-top: 30px;
}
</style>
