<template>
  <div class="home">

    <section class="hero is-small is-success">
      <div class="hero-body">
        <p class="title">Contacts Book</p>
        <p class="subtitle">This is small contacts book manager</p>
      </div>
    </section>

   

    <div class="columns is-desktop">
      <div class="column is-4">
        <div class="box">

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

  
      <div class="column">
        <div class="box">
          <div class="field is-grouped">
            <div class="control is-expanded is-fullwidth">
              <input class="input" type="text" placeholder="Search or Filter" v-model="search_term">
            </div>
            <div class="control">
              <a class="button is-info" v-on:click.prevent="getContactInfo">
                Search/Filter
              </a>
            </div>
          </div>
          <div class="cantact">
            <div class="card" v-for="contact in contacts" :key="contact.id">
              <div class="card-content">
                <div class="columns">
                  <div class="column is-one-fifth"><img src="../assets/ava.svg" width="150" height="150"></div>
                  <div class="column">
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
      </div>
    </div>

    <footer class="footer">
      <div class="content has-text-centered">
        <p>
          <strong>Create</strong> by <a href="#">Eldar Gazizov</a>. Copyright &#169; 2021
        </p>
      </div>
    </footer>

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

.box {
  margin-top: 20px;
  margin-right: 50px;
  margin-left: 50px;
}

.field {
  margin-top: -0.4rem;
}

.title {
  margin-top: 30px;
}

</style>
