<script setup>
import {computed, useTemplateRef} from "vue";
import InputFiled from "@/components/character/chat_field/input_field/InputFiled.vue";
import CharacterPhotoField from "@/components/character/chat_field/character_photo_field/CharacterPhotoField.vue";

const props = defineProps(['friend'])
const modalRef = useTemplateRef('modal-ref')

const modalStyle = computed(()=>{
  if(props.friend){
    return {
      backgroundImage: `url(${props.friend.character.background_image})`,
      backgroundSize: 'cover',
      backgroundRepeat: 'no-repeat',
      backgroundPosition: 'center',
    }
  }else{
    return {}
  }
})


function showModal(){
  modalRef.value.showModal()
}

defineExpose({
  showModal,
})
</script>

<template>
 <dialog ref="modal-ref" class="modal">
   <div class="modal-box w-90 h-150" :style="modalStyle">
     <button @click="modalRef.close()" class="btn btn-sm btn-ghost btn-circle bg-transparent absolute right-1 top-1">✕</button>
     <InputFiled/>
     <CharacterPhotoField v-if="friend" :character="friend.character"/>
   </div>
 </dialog>
</template>

<style scoped>

</style>