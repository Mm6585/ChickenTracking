<template>
        <v-card height="550" class="rounded-lg pa-0" outlined>
            
            <img src="http://192.168.0.246:8080/?action=stream">
        
        </v-card>
</template>
j
<script>
import { getDatabase, ref, onValue} from "firebase/database";


export default{
    data : () => ({

    }),
    methods : {
        
    },
    computed : {
        recentData : function() {
            const db = getDatabase();
            const ref = ref(db,'test')
            onValue(ref,(snapshot) => {
                this.data = snapshot.val();
                console.log(snapshot.val());
            })
            
        }
    }
}
</script>


<style>

</style>


    