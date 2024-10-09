package Day10.ClassWork.Annotations;


import java.lang.annotation.ElementType;
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.annotation.Target;

@Target({ElementType.METHOD, ElementType.FIELD}) // Notifies where the annotation will be used
@Retention(RetentionPolicy.RUNTIME)              // Defines the validity of annotation
public @interface CreatedBy {
    int priority();
    String createdBy();
}
