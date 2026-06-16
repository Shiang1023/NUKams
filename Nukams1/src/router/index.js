import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import LoginView from '../views/LoginView.vue'
import Login from '../components/Login.vue'
import Register from '../components/Register.vue'
import TCS_MainView from '../views/TCS_MainView.vue'
import TCS from '../views/TCS.vue'
import VisitRecordManager from '../views/visitRecordManager.vue'
import EditRecordSelectName from '../views/editRecordSelectName.vue'
import STS_MainView from '../views/STS_MainView.vue'
import STS from '../views/STS.vue'
import PersonalInfo_st from '../views/personalInfo_st.vue' 
import FillinRecord_st from '../views/FillinRecord_st.vue'
import VisitTime_st from '../views/VisitTime_st.vue'
import Repair_st from '../views/Repair_st.vue'
import Accommodation_st from '../views/Accommodation_st.vue'
import Advertisement from '../views/Advertisement.vue'
import AddAdvertisement from '../views/AddAdvertisement.vue'
import Post from '../views/Post.vue'
import CommentView from '../views/CommentView.vue'
import AddPost from '../views/AddPost.vue'
import StuManage from '../views/stuManage.vue'
import LDS_MainView from '../views/LDS_MainView.vue'
import LDS from '../views/LDS.vue'
import MaintanceNotice from '../views/MaintanceNotice.vue'
import LeaseAndRenter from '../views/LeaseAndRenter.vue'
import LDSPersonal from '../views/personalINFO_LDS.vue'
import ADS_MainView from '../views/ADS_MainView.vue'
import ADS from '../views/ADS.vue'
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      components: {default: HomeView}
    },
    {
      path: '/loginRegister',
      name: 'loginRegister',
      components: {default: LoginView},
      children: [
        {path: '', redirect: {name: 'login'},},
        {
          path: 'login',
          name: 'login',
          component: Login
        },
        {
          path: 'register',
          name: 'register',
          component: Register
        }
      ]
    },
    {
      path: '/TCSmain',
      name: 'TCSmain',
      components: { default: TCS_MainView },
      children: [
        { path: '', redirect: { name: 'TCS' } },
        {
          path: 'TCS/:username',
          name: 'TCS',
          component: TCS,
          children: [
            { path: 'visitRecordManager', name: 'visitRecordManager', component: VisitRecordManager },
            { path: 'fillRecordSelectName/:id', name: 'fillRecordSelectName', component: () => import('../views/fillRecordSelectName.vue') },
            { path: 'stuManage', name: 'stuManage', component: () => import('../views/stuManage.vue') },
            { path: 'personalINFO_tea/:id', name: 'personalINFO_tea', component: () => import('../views/personalINFO_tea.vue') },
            { path: 'editRecordSelectName/:id', name: 'editRecordSelectName', component: EditRecordSelectName },
            { path: 'StuPersonalSelectName/:id', name: 'StuPersonalSelectName', component: () => import('../views/StuPersonalSelectName.vue') },
            { path: 'StuAccSelectName/:id', name: 'StuAccSelectName', component: () => import('../views/StuAccSelectName.vue') },
            { path: 'StuRecordSelectName/:id', name: 'StuRecordSelectName', component: () => import('../views/StuRecordSelectName.vue') },
            { path: 'editRecord/:id/:name/:tid', name: 'editRecord', component: () => import('../views/editRecord.vue') },
            { path: 'fillRecord/:id/:name', name: 'fillRecord', component: () => import('../views/fillRecord.vue') },
            { path: 'StuInformation/:id/:name', name: 'StuInformation', component: () => import('../views/StuInformation.vue') },
            { path: 'StuRecord/:id/:name/:grade/:semester/:tid', name: 'StuRecord', component: () => import('../views/StuRecord.vue') },
            { path: 'StuAccInformation/:id/:name/:grade/:semester', name: 'StuAccInformation', component: () => import('../views/StuAccInformation.vue') },
          ]
        },
      ]
    },
    {
      path:'/STSmain',
      name: 'STSmain',
      components: {default: STS_MainView},
      children: [
        {path: '', redirect: {name: 'STS'},},
        {
          path: 'STS/:username',
          name: 'STS',
          component: STS,
          children: [
            {
              path: 'personalInfo_st/:st_id',
              name: 'personalInfo_st',
              component: PersonalInfo_st
            },
            {
              path: 'FillinRecord_st/:id',
              name: 'FillinRecord_st',
              component: FillinRecord_st
            },
            {
              path: 'VisitTime_st/:studentId',
              name: 'VisitTime_st',
              component: VisitTime_st
            },
            {
              path: 'Repair_st/:st_id',
              name: 'Repair_st',
              component: Repair_st
            },
            {
              path: 'Accommodation_st/:studentId/:academicYear/:semaster',
              name: 'Accommodation_st',
              component: Accommodation_st
            }
          ]
        }
      ]
    },
    {
      path:'/LDSmain',
      name: 'LDSmain',
      components: {default: LDS_MainView},
      children: [
        {path: '', redirect: {name: 'LDS'},},
      
        {
          path: 'LDS/:username',
          name: 'LDS',
          component: LDS,
          children: [
            {path: 'LeaseAndRenter/:id', name: 'LeaseAndRenter', component: LeaseAndRenter},
            {path: 'MaintanceNotice/:id', name: 'MaintanceNotice', component: MaintanceNotice},
            {path:'personalINFO_LDS/:id',name:'personalINFO_LDS',component:LDSPersonal},
          ]
        }
      ]
    },{
      path:'/ADSmain',
      name: 'ADSmain',
      components: {default: ADS_MainView},
      children: [
        {path: '', redirect: {name: 'ADS'},},
        {
          path: 'ADS/:username',
          name: 'ADS',
          component: ADS,
          children: [
            {path:'AccountManager_student',name:'AccountManager_student',component:()=>import('../views/AccountManager_student.vue')},
            {path:'AccountManager_teacher',name:'AccountManager_teacher',component:()=>import('../views/AccountManager_teacher.vue')},
            {path:'AccountManager_landlord',name:'AccountManager_landlord',component:()=>import('../views/AccountManager_landlord.vue')},
            {path:'VertifyManager_ad',name:'VertifyManager_ad',component:()=>import('../views/VertifyManager_ad.vue')},
            {path:'VertifyManager_post',name:'VertifyManager_post',component:()=>import('../views/VertifyManager_post.vue')},
            {path:'VertifyManager_comment',name:'VertifyManager_comment',component:()=>import('../views/VertifyManager_comment.vue')},
            {path:'DeleteManager_ad',name:'DeleteManager_ad',component:()=>import('../views/DeleteManager_ad.vue')},
            {path:'DeleteManager_post',name:'DeleteManager_post',component:()=>import('../views/DeleteManager_post.vue')},
            {path:'DeleteManager_comment',name:'DeleteManager_comment',component:()=>import('../views/DeleteManager_comment.vue')},
            {path:'personalINFO_ADS/:id',name:'personalINFO_ADS',component:()=>import('../views/personalINFO_ADS.vue')},
            {path:'personalINFO_student/:id',name:'personalINFO_student',component:()=>import('../views/personalINFO_student.vue')},
            {path:'personalINFO_teacher/:id',name:'personalINFO_teacher',component:()=>import('../views/personalINFO_teacher.vue')},
            {path:'personalINFO_landlord/:id',name:'personalINFO_landlord',component:()=>import('../views/personalINFO_landlord.vue')},
          ]
        }
      ]
    },
    {
      path:'/advertisement/:username',
      name: 'advertisement',
      components: {default: Advertisement}
    },{
      path:'/addAdvertisement/:username',
      name: 'AddAd',
      components: {default: AddAdvertisement}
    },
    {
      path:'/post',
      name: 'post',
      components: {default: Post}
    },
    {
      path:'/post/:username',
      name: 'post_self',
      components: {default: Post}
    },
    {
      path:'/comment/:username',
      name: 'comment',
      components: {default: CommentView}
    },
    {
      path:'/addPost/:username',
      name: 'addPost',
      components: {default: AddPost}
    }
  ]
})

export default router
