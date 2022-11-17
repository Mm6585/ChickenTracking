<template>
    <v-app id="stuRegister" class="primary">
        <v-content>
            <v-container fluid full-height>
                <v-layout align-center justify-center>
                    <v-flex xs12 sm8 md4 lg4>
                        <v-card class="elevation-1 pa-3">
                            <v-card-text>
                                <v-text-field prepend-icon="person" name="username" label="아이디 입력" type="text"
                                v-model="model.username"></v-text-field>
                                <v-text-field prepend-icon="lock" name="password" label="비밀번호 입력" id="password" type="password"
                                v-model="model.password"></v-text-field>
                            </v-card-text>          
                            <v-card-actions>
                            <v-spacer></v-spacer> 
                                <v-btn block color="primary" @click="login" :loading="loading">뒤로</v-btn>
                                <v-btn block color="primary" @click="signUp" >다음</v-btn>
                            </v-card-actions>
                        </v-card>
                    </v-flex>
                </v-layout>
            </v-container>
        </v-content>
    </v-app>
</template>

<script>
  import { getAuth, createUserWithEmailAndPassword } from "firebase/auth";
  import { getDatabase, ref, set } from "firebase/database";

  

  export default {
    layout: '/default',
    data: () => ({
      loading: false,
      model: {
        username: '',
        password: '',
      }
    }),
    methods: {
      login() {
        this.loading = true;
        setTimeout(() => {
          this.$router.push('/login');
        }, 1000);
      },
       signUp() {
          const db = getDatabase();
          // set(ref(db,'users/' + this.model.username.split('@')[0]) , {
          //   Name : this.model.stuName,
          //   stuNumber : this.model.stuNumber,
          //   Phone : this.model.stuPhone,
          //   profile_image : this.model.imageUrl
          // })

          //hash
          const crypto = require('crypto');
          const password = crypto.createHash('sha256').update(this.password).digest('base64');

          //Auth setting
          const auth = getAuth();
          createUserWithEmailAndPassword(auth, this.model.username, password)
          .then((userCredential) => {
          // Signed in
            const user = userCredential.user;
            console.log(user)
          // ...
          })
          .catch((error) => {
            prompt('다시 입력해주세요')
            const errorCode = error.code;
            console.log(errorCode)
            const errorMessage = error.message;
            console.log(errorMessage)
          // ..
          this.loading=true;
          setTimeout(() => {
          this.$router.push('/SuccessRegister');
          }, 1000);
          })


       },
        
        upload(e) { 
            let imageFile = e.target.files 
            console.log(imageFile[0])
            let url = URL.createObjectURL(imageFile[0]) 
            console.log(url) 
            this.model.imageUrl = url
        } 
    }
  };
  
</script>


<style scoped lang="css">
  #stuRegister {
    height: 100%;
    width: 100%;
    position: absolute;
    top: 0;
    left: 0;
    content: "";
    z-index: 0;
  }
</style>