### Struct for Custom Resource Definition (CRD)
```go
type MyApp struct {
    metav1.TypeMeta   `json:",inline"`
    metav1.ObjectMeta `json:"metadata,omitempty"`
    
    Spec   MyAppSpec   `json:"spec,omitempty"`
    Status MyAppStatus `json:"status,omitempty"`
}

type MyAppSpec struct {
    Replicas int    `json:"replicas"`
    Image    string `json:"image"`
    Version  string `json:"version"`
}

type MyAppStatus struct {
    AvailableReplicas int    `json:"availableReplicas"`
    State             string `json:"state"`
}
```

### Public / Private
```go
package models

type User struct {
    ID        int    // Public field (Upper case)
    Username  string // Public field
    Email     string // Public field
    password  string // Private field (normal case)
}
```