<script setup>

import Name from "@/views/create/charater/components/Name.vue";
import Profile from "@/views/create/charater/components/Profile.vue";
import BackgroundImage from "@/views/create/charater/components/BackgroundImage.vue";
import Photo from "@/views/create/charater/components/Photo.vue";
import {ref, useTemplateRef} from "vue";
import {base64ToFile} from "@/js/utils/base64_to_file.js";
import api from "@/js/http/api.js";
import {useRouter} from "vue-router";
import {useUserStore} from "@/stores/user.js";

const user=useUserStore()
const router = useRouter();
const photoRef = useTemplateRef('photo-ref')
const nameRef = useTemplateRef('name-ref')
const profileRef = useTemplateRef('profile-ref')
const backgroundImageRef = useTemplateRef('background-image-ref')
const errorMessage  = ref('')
async function handleCreate(){
  const photo = photoRef.value.myPhoto
  const name = nameRef.value.myName?.trim()
  const profile = profileRef.value.myProfile?.trim()
  const backgroundImage = backgroundImageRef.value.myBackgroundImage

  if(!photo){
    errorMessage.value = '角色头像不能为空'
  }
  else if(!name){
    errorMessage.value = '角色名称不能为空'
  }
  else if(!profile){
    errorMessage.value = '角色简介不能为空'
  }
  else if(!backgroundImage){
    errorMessage.value = '背景图片不能为空'
  }
  const formData = new FormData()

  formData.append("name",name)
  formData.append('profile',profile)
  formData.append("background_image",base64ToFile(backgroundImage,'background_image.png'))
  formData.append("photo",base64ToFile(photo,'photo.png'))

  try{
    const res = await api.post('/api/create/character/create/',formData )
    const data = res.data
    if(data.result==='success'){
       errorMessage.value='success'
       await router.push({
         name:'user-space-index',
         params:{
           user_id:user.id
         }
       })
    }else{
      errorMessage.value =data.result
    }
  }catch(err){
    console.log(err)
  }


}
</script>

<template>
  <div class="flex justify-center">
    <div class="card w-120 bg-base-200 shadow-sm mt-16">
      <div class="card-body">
        <h3 class="text-lg font-bold my-4">创建角色</h3>
        <Photo ref="photo-ref"/>
        <name ref="name-ref"/>
        <Profile ref="profile-ref"/>
        <BackgroundImage ref="background-image-ref"/>
        <p v-if="errorMessage" class="text-red-500 text-sm">{{errorMessage}}</p>
        <div class="flex justify-end">
          <button @click="handleCreate" class="btn btn-neutral w-60 mt-2">创建</button>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>

</style>