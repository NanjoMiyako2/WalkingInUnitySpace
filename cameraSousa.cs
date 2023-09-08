using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System.Threading;
using System.Threading.Tasks;
 
public class CameraScript : MonoBehaviour
{
    [SerializeField] GameObject player;
 
 	void Start(){
 	
 	    Screen.SetResolution(960, 540, FullScreenMode.Windowed, 60);
 	
        // transformを取得
        Transform myTransform = this.transform; 	
        // ローカル座標を基準に、回転を取得
        Vector3 localAngle = myTransform.localEulerAngles;
        localAngle.x = .0f; // ローカル座標を基準に、x軸を軸にした回転を0度に変更
        localAngle.y = .0f; // ローカル座標を基準に、y軸を軸にした回転を0度に変更
        localAngle.z = .0f; // ローカル座標を基準に、z軸を軸にした回転を0度に変更
        myTransform.localEulerAngles = localAngle; // 回転角度を設定
 	
 	}
 	
    void Update()
    {
        // transformを取得
        Transform myTransform = this.transform;
        Vector3 localAngle = myTransform.localEulerAngles;


        // 左に移動
        if (Input.GetKey (KeyCode.Alpha0)) {
            this.transform.Translate (-0.1f,0.0f,0.0f);
        }
        // 右に移動
        if (Input.GetKey (KeyCode.Alpha1)) {
            this.transform.Translate (0.1f,0.0f,0.0f);
        }
        // 前に移動
        if (Input.GetKey (KeyCode.Alpha2)) {
            this.transform.Translate (0.0f,0.0f,0.1f);
        }
        
        // 後ろに移動
        if (Input.GetKey (KeyCode.Alpha3)) {
            this.transform.Translate (0.0f,0.0f,-0.1f);
        }
        
        //左に回転
        if(Input.GetKey(KeyCode.Alpha4)){
        	localAngle.x = 0.0f; // ローカル座標を基準に、x軸を軸にした回転を10度に変更
        	localAngle.y -= 1.0f; // ローカル座標を基準に、y軸を軸にした回転を10度に変更
        	localAngle.z = 0.0f; // ローカル座標を基準に、z軸を軸にした回転を10度に変更
            myTransform.localEulerAngles = localAngle; // 回転角度を設定
            
            
            if(localAngle.y < -360.0f){
            	localAngle.y += 360.0f;
            }

    
        }
        
        
        //右に回転
        if(Input.GetKey(KeyCode.Alpha5)){
        	localAngle.x = 0.0f; // ローカル座標を基準に、x軸を軸にした回転を10度に変更
        	localAngle.y += 1.0f; // ローカル座標を基準に、y軸を軸にした回転を10度に変更
        	localAngle.z = 0.0f; // ローカル座標を基準に、z軸を軸にした回転を10度に変更
            myTransform.localEulerAngles = localAngle; // 回転角度を設定
            
            
            if(localAngle.y > 360.0f){
            	localAngle.y += -360.0f;
            }
            
        
        }
        
         //上に回転
        if(Input.GetKey(KeyCode.Alpha6)){
        	localAngle.x += -1.0f; // ローカル座標を基準に、x軸を軸にした回転を10度に変更
        	localAngle.y = 0.0f; // ローカル座標を基準に、y軸を軸にした回転を10度に変更
        	localAngle.z = 0.0f; // ローカル座標を基準に、z軸を軸にした回転を10度に変更
            myTransform.localEulerAngles = localAngle; // 回転角度を設定
            
            if(localAngle.x < -360.0f){
            	localAngle.x += 360.0f;
            }
            
    
        }
        
        
        //下に回転
        if(Input.GetKey(KeyCode.Alpha7)){
        	localAngle.x += 1.0f; // ローカル座標を基準に、x軸を軸にした回転を10度に変更
        	localAngle.y = 0.0f; // ローカル座標を基準に、y軸を軸にした回転を10度に変更
        	localAngle.z = 0.0f; // ローカル座標を基準に、z軸を軸にした回転を10度に変更
            myTransform.localEulerAngles = localAngle; // 回転角度を設定
            
            if(localAngle.x > 360.0f){
            	localAngle.x += -360.0f;
            }
            
        
        }
        
        Thread.Sleep(500);
        
    }
}